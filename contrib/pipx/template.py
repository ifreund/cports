pkgname = "pipx"
pkgver = "1.3.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-pytest",
]
depends = [
    "python-argcomplete",
    "python-colorama",
    "python-packaging",
    "python-platformdirs",
    "python-userpath",
]
pkgdesc = "Python tool for installing binaries to venvs"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/pypa/pipx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "256f5b70a40a32fde4eb3bf5c4ed7b735313bf0cda8b52912ce9b2014f35f250"
# missing some unknown deps
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
