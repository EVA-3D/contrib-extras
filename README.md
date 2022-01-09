# EVA-3D community contributions
This is the place that houses the community contributions that do not necessarily conform 100% to the standard EVA defines, but may still be useful in specific applications. This is also a place to share other things like spool holders, test prints, etc. If you have a part or a mod you want to list here, fork this repository, add your files, and [submit a pull request](https://github.com/EVA-3D/contrib-extras/pulls). Anyone is welcome to contribute, in fact, the more the merrier!

# How to contribute
Fork this repository and add your stls, an image preview and a page file for presenting your part.

Part descriptions are written in markdown (.md) files.

* The main page for your part should be in `docs/[category]/[your_part_name].md`
* Any assets linked from that page (images, etc) should be in `docs/[category]/assets`. All files should be prefixed with your part name.
* The STL(s) should be in `docs/[category]/stl`. All files should be prefixed with your part name.
* Take a look at [Pawel's Spool Holder](https://github.com/EVA-3D/contrib-extras/tree/main/docs/spool_holders) for inspiration.

If you're not familiar with Git, reach out to `@miklschmidt#2036` on discord, or get help on [the unofficial Rat Rig discord server](https://discord.gg/D62e8XNeYa).

Please note that all contributes are automatically subject to the terms of the [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).

Please! Share your candy!

![candy](docs/assets/candy_bowl.png)

## Local deployment 

There are two options, either you have a local Python envorinment with `Python` and `Poetry` or you can use Docker - the latter is easier but will be troublesome on Windows (since Windows is troublesome).

To get Docker go to https://docs.docker.com/get-docker/ and proceed with the installation steps. Do not be affraid in case you see this as black magic, Docker is a tool that allowes to run a tiny version of a Linux system on Mac, Windows and Linux - that tindy system is isolated from your machine - it's like a sandbox for developers.

> Per the documentation:
> It remains free for small businesses (fewer than 250 employees AND less than $10 million in annual revenue), **personal use**, education, and **non-commercial open source projects**.

Once it's installed you can use Docker Compose to deploy your own private EVA contrib site that will be visible only to you, go ahead and experiment with it to make sure your changes work before making a pull request :)

```
docker-compose up
```

And your local site will be accessible on the 127.0.0.1 address with is the loopback address pointing to your own machine: http://127.0.0.1:62999 is the full address and port.
