


/*Gets list of modules in order to create default workspace directory*/

async function getModules(){
    let url = "http://192.168.1.149:8000/api/modules/";
    try{
        let res = await fetch(url);
        return await res.json();
    }
    catch(error){
        console.log(error);
    }
}
function getModuleNames(modules){
    const modules = getModules();
    const module_titles = [];
    for (module of modules){
        const module_title = module["title"];
        module_titles.push(module_title);
    }
    return module_titles;
}
function getModulePaths(){
    const module_names = getModuleNames();
    const prefix = "/root/";
    const module_paths = [];
    for (module_name of module_names){
        const module_path = prefix + module_name;
        module_paths.push(module_path);
    }
    return module_paths;
}
function getModuleDirs(module_paths){
    const trees = [];
    for (module_path of module_paths){
        const tree = {
            module_path: {
                path: module_path,
                type: "module",
                children: [
                    module_path + "/bots",
                    module_path + "/data_objects",
                    module_path + "/reports"
                ]
            }
        }
        trees.push(tree);
    }
    return trees
}
function getDefaultWorkspaceDir(module_dirs){
    modules = []
    const tree_data = {
        "/root": {
            path: "/root",
            type: "folder",
            isRoot: true,
            children: getModulePaths()
        }

    }
    for (module_dir of module_dirs){
        tree_data.push(module_dir)
    }
    return tree_data
    
}
const module_paths = getModulePaths();
const module_dirs = getModuleDirs(module_paths);
const default_workspace_dir = getDefaultWorkspaceDir(module_dirs);
console.log(default_workspace_dir);





