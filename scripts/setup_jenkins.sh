#!/bin/bash

# Install Jenkins
echo "Installing Jenkins..."
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install -y jenkins

# Start Jenkins
echo "Starting Jenkins..."
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Get initial admin password
echo "Getting initial admin password..."
INITIAL_PASSWORD=$(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)
echo "Initial admin password: $INITIAL_PASSWORD"
echo "Please save this password and use it to set up Jenkins at http://localhost:8080"

# Install required packages
echo "Installing required packages..."
sudo apt-get install -y docker.io
sudo usermod -aG docker jenkins
sudo usermod -aG docker $USER

# Restart Jenkins to apply changes
echo "Restarting Jenkins..."
sudo systemctl restart jenkins

echo "Jenkins setup complete!"
echo "Please follow these steps:"
echo "1. Access Jenkins at http://localhost:8080"
echo "2. Install suggested plugins"
echo "3. Create admin user"
echo "4. Install additional plugins: Git, Pipeline, Docker Pipeline, Kubernetes CLI"
echo "5. Configure credentials for DockerHub and GitHub"
echo "6. Create new pipeline job using the Jenkinsfile in this repository" 