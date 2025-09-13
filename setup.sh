#!/usr/bin/env bash

# me-cli Automatic Installation Script
# Compatible with Ubuntu and Termux

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to detect environment
detect_environment() {
    if command -v pkg &> /dev/null; then
        echo "termux"
    elif command -v apt &> /dev/null; then
        echo "ubuntu"
    else
        echo "unknown"
    fi
}

# Function to check if command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Function to install dependencies for Termux
install_termux_deps() {
    print_status "Installing dependencies for Termux..."
    
    print_status "Updating package lists..."
    pkg update -y
    
    print_status "Installing Python..."
    pkg install python -y
    
    print_status "Installing Git..."
    pkg install git -y
    
    print_status "Installing additional dependencies..."
    pkg install python-pillow -y
    
    print_success "Termux dependencies installed successfully!"
}

# Function to install dependencies for Ubuntu
install_ubuntu_deps() {
    print_status "Installing dependencies for Ubuntu..."
    
    print_status "Updating package lists..."
    sudo apt update
    
    print_status "Installing Python and pip..."
    sudo apt install -y python3 python3-pip
    
    print_status "Installing Git..."
    sudo apt install -y git
    
    print_status "Installing additional dependencies..."
    sudo apt install -y python3-dev build-essential
    
    print_success "Ubuntu dependencies installed successfully!"
}

# Function to setup environment file
setup_environment() {
    local install_dir="$HOME/me-cli"
    local env_file="$install_dir/.env"
    local env_template="$install_dir/.env.template"
    
    if [ ! -f "$env_file" ] && [ -f "$env_template" ]; then
        print_status "Setting up environment configuration..."
        cp "$env_template" "$env_file"
        print_warning "Please edit ~/.me-cli/.env and configure your API settings before running me-cli"
        print_status "You can edit the file with: nano ~/.me-cli/.env"
    fi
}

# Function to install Python requirements
install_python_deps() {
    print_status "Installing Python dependencies..."
    
    local pip_cmd
    if command_exists pip3; then
        pip_cmd="pip3"
    elif command_exists pip; then
        pip_cmd="pip"
    else
        print_error "Neither pip nor pip3 found!"
        exit 1
    fi
    
    $pip_cmd install --upgrade pip
    $pip_cmd install -r requirements.txt
    
    print_success "Python dependencies installed successfully!"
}

# Function to clone or update repository
setup_repository() {
    local repo_url="https://github.com/wayme14/me.git"
    local install_dir="$HOME/me-cli"
    
    if [ -d "$install_dir" ]; then
        print_warning "Directory $install_dir already exists. Updating..."
        cd "$install_dir"
        git pull origin main
    else
        print_status "Cloning me-cli repository..."
        git clone "$repo_url" "$install_dir"
        cd "$install_dir"
    fi
    
    print_success "Repository setup completed!"
}

# Function to create convenient access
create_access() {
    local install_dir="$HOME/me-cli"
    local python_cmd
    
    if command_exists python3; then
        python_cmd="python3"
    elif command_exists python; then
        python_cmd="python"
    else
        print_error "Python not found!"
        exit 1
    fi
    
    # Create a wrapper script
    local wrapper_script="$HOME/.local/bin/me-cli"
    mkdir -p "$HOME/.local/bin"
    
    cat > "$wrapper_script" << EOF
#!/bin/bash
cd "$install_dir"
$python_cmd main.py "\$@"
EOF
    
    chmod +x "$wrapper_script"
    
    # Add to PATH if not already there
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.profile" 2>/dev/null || true
        print_status "Added $HOME/.local/bin to PATH. Please restart your shell or run: source ~/.bashrc"
    fi
    
    print_success "me-cli command created! You can now run 'me-cli' from anywhere."
}

# Main installation function
main() {
    print_status "Starting me-cli installation..."
    
    # Detect environment
    local env=$(detect_environment)
    print_status "Detected environment: $env"
    
    case $env in
        "termux")
            install_termux_deps
            ;;
        "ubuntu")
            install_ubuntu_deps
            ;;
        "unknown")
            print_error "Unsupported environment. This script supports Ubuntu and Termux only."
            exit 1
            ;;
    esac
    
    # Setup repository
    setup_repository
    
    # Install Python dependencies
    install_python_deps
    
    # Setup environment configuration
    setup_environment
    
    # Create convenient access
    create_access
    
    print_success "me-cli installation completed successfully!"
    print_status "You can now run the application with:"
    print_status "  cd ~/me-cli && python3 main.py"
    print_status "Or simply: me-cli (after restarting your shell)"
    print_status ""
    print_warning "IMPORTANT: Configure your .env file before first use!"
    print_status "Edit ~/me-cli/.env with your API settings"
    print_status "Don't forget to get your API key from @fykxt_bot on Telegram!"
}

# Run main function
main "$@"