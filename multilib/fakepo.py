class FakePackageObject(object):
    """
    fake package object that contains enough data to run through the testing
    framework herein
    """
    def __init__(self, po=None, d=None, pkg=None):
        # FPO's can be created from yum Package Objects or dictionaries
        if po:
            self.name = po.name
            self.arch = po.arch
            self.provides = list(filter_yum_reldeps(po.provides))
            self.requires = list(filter_yum_reldeps(po.requires))
            self.files = po.returnFileEntries()
        elif d:
            self.name = d['name']
            self.arch = d['arch']
            self.provides = d['provides']
            self.requires = d['requires']
            self.files = d['files']
        elif pkg:
            self.name = pkg.name
            self.arch = pkg.arch
            self.provides = [str(x).split()[0] for x in pkg.provides]
            self.requires = [str(x).split()[0] for x in pkg.requires]
            self.files = pkg.files
        else:
            raise RuntimeError('fake package objects must come from a real yum object or dictionary')

    def convert(self):
        return {
            'name': self.name,
            'arch': self.arch,
            'provides': self.provides,
            'requires': self.requires,
            'files': self.files
        }

    def returnFileEntries(self):
        return self.files


def filter_yum_reldeps(provides):
    for (p_name, p_flag, (p_e, p_v, p_r)) in provides:
        yield p_name
