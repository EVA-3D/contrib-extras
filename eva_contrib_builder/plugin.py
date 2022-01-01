import logging

from mkdocs.plugins import BasePlugin
from mkdocs.exceptions import BuildError
from mkdocs.utils.meta import YAML_RE
import yaml
try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader

from eva_contrib_builder.schemas import EasyPageMeta


log = logging.getLogger(__name__)



# TODO: Decide if it's even helpful
# import click
# from mkdocs.__main__ import ColorFormatter
# mkdocs_logger = logging.getLogger("mkdocs")
# class GHActionsColorFormatter(ColorFormatter):

#     PREFIX_LEVELS = {
#         "WARNING": "::error::",
#         "ERROR": "::error::",
#     }

#     def format(self, record):
#         message = super().format(record)
#         prefix = ""
#         if record.levelname in self.PREFIX_LEVELS:
#             prefix = self.PREFIX_LEVELS[record.levelname]
#         return prefix + message
# mkdocs_logger.handlers[0].setFormatter(GHActionsColorFormatter())

class EVAContribPlugin(BasePlugin):
    
    def on_config(self, config):
        self.env = config['theme'].get_env()
        self.env.filters["yes_no"] = self.yes_no

    @staticmethod
    def yes_no(value: bool):
        return "yes" if value else "no"

    def _get_markdown_context(self, page, config):
        page.eva = None
        if "eva" in page.meta:
            page.eva = EasyPageMeta(**page.meta["eva"])

        return {
            "eva": page.eva,
        }

    def on_page_context(self, context, page, config, nav):
        context = {**self._get_markdown_context(page, config), **context}
        return context

    def on_page_read_source(self, page, config):
        # Mkdocs hides YAML parsing errors, to access those I need to load the 
        # source and do an initial YAML load on my own, it get properly loded 
        # again by mkdocs
        try:
            with open(page.file.abs_src_path, 'r', encoding='utf-8-sig', errors='strict') as f:
                source = f.read()
        except OSError:
            log.error(f'File not found: {page.file.src_path}')
            raise
        except ValueError:
            log.error(f'Encoding error reading file: {page.file.src_path}')
            raise

        m = YAML_RE.match(source)
        if m:
            try:
                data = yaml.load(m.group(1), SafeLoader)
                if not isinstance(data, dict):
                    data = {}
            except Exception as exc:
                raise BuildError(f"Page's YAML metadata is malformed: {exc}")
            page.meta = data
        return source

    def on_page_markdown(self, markdown, page, config, files):
        md_template = self.env.from_string(markdown)
        return md_template.render(**self._get_markdown_context(page, config))
