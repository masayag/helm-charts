import os

import pytest
from pathlib import Path

from container_ci_suite.helm import HelmChartsAPI

test_dir = Path(os.path.abspath(os.path.dirname(__file__)))


class TestHelmRHELNodeJSImageStreams:

    def setup_method(self):
        package_name = "nodejs-imagestreams"
        path = test_dir / "../charts/redhat"
        self.hc_api = HelmChartsAPI(path=path, package_name=package_name, tarball_dir=test_dir)

    def teardown_method(self):
        self.hc_api.delete_project()

    @pytest.mark.parametrize(
        "version,registry",
        [
            ("16-ubi9", "registry.redhat.io/ubi9/nodejs-16:latest"),
            ("16-ubi9-minimal", "registry.redhat.io/ubi9/nodejs-16-minimal:latest"),
            ("16-ubi8", "registry.redhat.io/ubi8/nodejs-16:latest"),
            ("16-ubi8-minimal", "registry.redhat.io/ubi8/nodejs-16-minimal:latest"),
            ("14-ubi7", "registry.redhat.io/ubi7/nodejs-14:latest"),
        ],
    )
    def test_package_imagestream(self, version, registry):
        self.hc_api.set_version("0.0.1")
        self.hc_api.helm_package()
        self.hc_api.helm_installation()
        assert self.hc_api.check_imagestreams(version=version, registry=registry)


class TestHelmCentOSNodeJSImageStreams:

    def setup_method(self):
        package_name = "nodejs-imagestreams"
        path = test_dir / "../charts/centos"
        self.hc_api = HelmChartsAPI(path=path, package_name=package_name, tarball_dir=test_dir)

    def teardown_method(self):
        self.hc_api.delete_project()

    @pytest.mark.parametrize(
        "version,registry",
        [
            ("16-ubi9", "registry.access.redhat.com/ubi9/nodejs-16:latest"),
            ("16-ubi9-minimal", "registry.access.redhat.com/ubi9/nodejs-16-minimal:latest"),
            ("16-ubi8", "registry.access.redhat.com/ubi8/nodejs-16:latest"),
            ("16-ubi8-minimal", "registry.access.redhat.com/ubi8/nodejs-16-minimal:latest"),
            ("14-ubi8", "registry.access.redhat.com/ubi8/nodejs-14:latest"),
            ("14-ubi8-minimal", "registry.access.redhat.com/ubi8/nodejs-14-minimal:latest"),
            ("14-ubi7", "registry.access.redhat.com/ubi7/nodejs-14:latest"),
        ],
    )
    def test_package_imagestream(self, version, registry):
        self.hc_api.set_version("0.0.1")
        self.hc_api.helm_package()
        self.hc_api.helm_installation()
        assert self.hc_api.check_imagestreams(version=version, registry=registry)
