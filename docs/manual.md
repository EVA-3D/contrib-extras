---
title: Example page
icon: material/head-question
eva: 
    author:
        display_name: Paweł Kucmus
        url: https://github.com/pkucmus
    description: | 
        If you put a pipe `|` followed by a line break you can do a multiline description.
        This supports markdown so you can put a:

        - list
        - image
        - many other

        Go to the [:material-github: source of this file](https://github.com/EVA-3D/contrib-extras/edit/main/docs/index.md) to see how it works.

        Have fun: ![](assets/candy_bowl.png)
    bom:
        - name: my_custom_part
          qty: 1
          is_printable: true
          url: assets/fake_stl.stl
        - name: some screw
          qty: 12
          is_printable: false
    eva_version: "2.0.0 and up"
    print_instructions: | 
        There are none, this is an example page
    step_files: |
        None
---

{% extends "easy_page.html" %}
