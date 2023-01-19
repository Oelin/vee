# Vee: The Universal Package Installer 

❤🧡💛💚💙💜

Vee is a simple CLI script for installing packages via GitHub and other generic repositories. It essentially combines the process of downlading and then installing a package into a one, tiny command. 

```sh
vee [owner]/[package]
```


## Installation

Install Vee with `pip`

```sh
pip install git+https://github.com/Oelin/vee
```

Install Vee with Vee

```
vee oelin/vee
```


## vee.py

Packages which require specific commands to execute during the build process must include a `vee.py` file in their root directory. This file contains code which executes after the package is downloaded. For instance it might set some environment variables, or (more commonly) call an external build tool (npm, poetry, docker etc). 
