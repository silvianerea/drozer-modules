from drozer.modules import common, Module
from drozer import android

class Cloak_Dagger1(Module, common.PackageManager):
    name = "Check if the apk has the permission to perform a Cloak and Dagger attack"
    description = "Check if the apk has the permission to perform a Cloak and Dagger attack"
    examples = '''
    dz> run silvia.cloakdagger -a com.mwr.example.sieve
    '''
    author = "Silvia (@silvianerea)"
    date = "2017-06-07"
    path = ["silvia"]
    permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]
    PERMISSION1_SYSTEM = "SYSTEM_ALERT_WINDOW"
    PERMISSION2_ACCESSIBILITY = "BIND_ACCESSIBILITY_SERVICE"

    def execute(self, arguments):
        con = self.getContext()
        pm = con.getPackageManager()
        res = con.getResources()

        permissionList = []

        # Iterate through each package and get unique permissions
        self.stdout.write("Applications that could be malicious and take advantage of Cloak and Dagger exploit:\n")
        for package in self.packageManager().getPackages(common.PackageManager.GET_PERMISSIONS):
            if package.requestedPermissions != None:
                for permission in package.requestedPermissions:
                    if permission not in permissionList:
                        permissionList.append(str(permission))
                if self.PERMISSION1_SYSTEM in str(permissionList) and self.PERMISSION2_ACCESSIBILITY in str(permissionList):
                    self.stdout.write(" +[color green]" + str(package.packageName) + "[/color]\n")
                    self.stdout.write(" Permissions:\n")
                    for permission in permissionList:
                        self.stdout.write(" -" + permission + "\n")
                permissionList = []