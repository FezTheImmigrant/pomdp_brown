FROM ubuntu:latest

ENV DOCKER_USER developer

# Create user with passwordless sudo. This is only acceptable as it is a
# private dev env not exposed to the outside world. Do
# NOT do this on your host machine or otherwise
RUN apt-get update 
RUN apt-get install -y sudo 
RUN adduser --disabled-password --gecos '' "$DOCKER_USER" 
RUN adduser "$DOCKER_USER" sudo 
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers 
RUN touch home/$DOCKER_USER/.sudo_as_admin_successful 
RUN rm -rf /var/lib/apt/lists/*

USER "$DOCKER_USER"

WORKDIR "/home/$DOCKER_USER"


# need curl to automatically install vim-plug
# need clang-format for formatting c# files
# need black for formatting python files
RUN sudo apt-get update 
RUN sudo apt-get install -y neovim 
RUN sudo apt-get install -y git 
RUN sudo apt-get install -y curl 
RUN sudo apt-get install -y clang-format 
RUN sudo apt-get install -y black 
RUN sudo apt-get install -y python3-pip 
    

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
RUN sudo apt-get install -y nodejs

RUN git clone https://github.com/FezTheImmigrant/nvim.git ~/.config/nvim

#install ripgrep
RUN sudo dpkg -i ~/.config/nvim/ripgrep_12.1.1_amd64.deb

# Install Plugins for neovim that way when I close the constainer, I dont have to reinstall the plugins
RUN nvim +'PlugInstall --sync ' +qa

# need to UpdateRemotePlugins for semshi. Plug-Config isn't working as intended
RUN nvim +"PlugUpdate --sync | UpdateRemotePlugins" +qa

