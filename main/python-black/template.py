pkgname = "python-black"
pkgver = "23.12.0"
pkgrel = 0
build_style = "python_pep517"
make_check_env = {"PYTHONPATH": "src"}
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
depends = [
    "python-click",
    "python-mypy_extensions",
    "python-packaging",
    "python-pathspec",
    "python-platformdirs",
]
checkdepends = [
    "python-aiohttp",
    "python-ipython",
    "python-pytest",
    "python-pytest-xdist",
    "python-tokenize_rt",
] + depends
pkgdesc = "Python formatting tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://black.readthedocs.io"
source = f"$(PYPI_SITE)/b/black/black-{pkgver}.tar.gz"
sha256 = "330a327b422aca0634ecd115985c1c7fd7bdb5b5a2ef8aa9888a82e2ebe9437a"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
