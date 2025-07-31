import os
import importlib.util
# from ai_shell.module_loader import discover_modules
# If 'module_loader.py' is in the same directory, use:
from module_loader import discover_modules  # Use absolute import if running as a script
# Or, if 'module_loader.py' is in a subdirectory named 'ai_shell', use:
# from ai_shell.module_loader import discover_modules
# Or, if it's in a subdirectory named 'ai_shell', ensure there's an __init__.py file in 'ai_shell' and use:
# from ai_shell.module_loader import discover_modules

LOG_PATH = "ai_shell/run_log.txt"

def log(msg):
    with open(LOG_PATH, "a") as f:
        f.write(f"{msg}\n")
    print(msg)

def run_module(module_path):
    name = os.path.splitext(os.path.basename(module_path))[0]
    spec = importlib.util.spec_from_file_location(name, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    log(f"✅ Ran module: {module_path}")

def main():
    print("🧠 AI Security Shell")
    modules = discover_modules()
    
    print("\nModules found:")
    for i, (mod_type, mod_path) in enumerate(modules):
        print(f"{i+1}. [{mod_type.upper()}] {os.path.basename(mod_path)}")

    try:
        choice = int(input("\nEnter module number to run: ")) - 1
        run_module(modules[choice][1])
    except:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as f:
            f.write("AI Security Shell Run Log\n")
            f.write("=" * 30 + "\n")
    log("AI Security Shell started.")
    log("Use 'discover_modules' to find and run security modules.")
    log("Modules can be added to the 'modules' directory.")
    log("Check the run log at 'ai_shell/run_log.txt' for details.")