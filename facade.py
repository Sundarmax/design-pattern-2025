from symtable import Class

# SubSystem classes.
class CodeBuilder:
    def build(self):
        print("Building the source code..")
        print("Build successful")
class Tester:
    def run_test(self):
        print("Running the testing")
        print("All test passed")
class Packager:
    def create_image(self):
        print("Creating a docker image")
        print("Pushing the image to ECR. DONE")
class Deployer:
    def run_deploy(self,image=None,target_server=None):
        print("Deployment successful")
    def roll_back(self):
        print("Rolling back deployment")
        print("Rollbck completed successfully")

# facade class
class DeploymentFacade:

    def __init__(self,target_server=None):
        self.code_build = CodeBuilder()
        self.test = Tester()
        self.package = Packager()
        self.deploy = Deployer()
        self.target_server = target_server

    def deploy_application(self):
        try:
            print("Starting the application deployment")
            self.code_build.build()
            self.test.run_test()
            self.package.create_image()
            self.deploy.run_deploy(target_server=self.target_server)
            print("Deployment is completed")
        except Exception as err:
            print("Unable to complete the deployment. hence rolling back")
            self.deploy.roll_back()
            print("Roll back is done")

if __name__ == "__main__":
    # facade client
    deploy = DeploymentFacade()
    deploy.deploy_application()