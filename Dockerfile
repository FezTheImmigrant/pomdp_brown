FROM ubuntu:latest

ENV DOCKER_USER developer

# Create user with passwordless sudo. This is only acceptable as it is a
# private dev env not exposed to the outside world. Do
# NOT do this on your host machine or otherwise
RUN apt-get update && \
    apt-get install -y sudo && \
    adduser --disabled-password --gecos '' "$DOCKER_USER" && \
    adduser "$DOCKER_USER" sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    touch home/$DOCKER_USER/.sudo_as_admin_successful && \
    rm -rf /var/lib/apt/lists/*

USER "$DOCKER_USER"

WORKDIR "/home/$DOCKER_USER"


# need curl to automatically install vim-plug
# need clang-format for formatting c# files
# need black for formatting python files
RUN sudo apt-get update && \
    sudo apt-get install -y neovim && \
    sudo apt-get install -y git && \
    sudo apt-get install -y curl && \
    sudo apt-get install -y clang-format && \
    sudo apt-get install -y black && \
    sudo apt-get install -y python3-pip && \
    sudo apt-get install -y python2.7
    

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
RUN sudo apt-get install -y nodejs

RUN git clone https://github.com/FezTheImmigrant/nvim.git ~/.config/nvim

#install ripgrep
RUN sudo dpkg -i ~/.config/nvim/ripgrep_12.1.1_amd64.deb

# Install Plugins for neovim that way when I close the constainer, I dont have to reinstall the plugins
RUN nvim +'PlugInstall --sync' +qa

