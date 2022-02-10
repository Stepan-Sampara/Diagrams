from diagrams import Diagram, Cluster
from diagrams.custom import Custom

with Diagram(" Terraform - creates 2 hosts, Ansible - configuring hosts (DB and Geo app), Jenkins - runner for Terraform and Ansible", show=False, filename="custom_local", direction="LR"):
    jenkins = Custom("Jenkins", "jenkins_logo_icon_170552.png") 
    ansible = Custom("Ansible", "Ansible_logo.svg.png")
    with Cluster("Terraform"):
         group = [Custom("DB", "file_type_terraform_icon_130125.png"),
                  Custom("APP", "file_type_terraform_icon_130125.png")]
    jenkins >> ansible >> group
    jenkins << ansible << group
