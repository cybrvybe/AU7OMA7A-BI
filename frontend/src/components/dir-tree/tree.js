
import axios from "axios";
import React from "react";

export default class Tree extends React.Component{
    constructor(props) {
        super(props);

        this.state = {
            modules: [],
            dir_tree: [],
            module_paths: [],
            bots: [],
            reports: [],
            isLoading: true
        };
    }
    
    async componentDidMount(){
        let modules_url = "http://192.168.1.149:8000/api/modules/";
        let bots_url = "http://192.168.1.149:8000/api/bots/";
        let reports_url = "http://192.168.1.149:8000/api/reports/";
        /*let data_models_url = "http://192.168.1.149:8000/api/modules/";*/ 
        
        var modules_res = await axios.get(modules_url);
        
        var bots_res = await axios.get(bots_url);
        
        var reports_res = await axios.get(reports_url);
        this.setState(
            {
                modules: Array.from(modules_res),
                reports: Array.from(reports_res),
                bots: Array.from(bots_res)
            }
        )
        
    
        
        
    };
    
  
    getModulePaths(modules = []){
        const module_titles = [];
        for (const module of modules){
            const module_title = module["title"];
            module_titles.push(module_title);
        }
        const prefix = "/root/";
        const module_paths = [];
        for (const module_title of module_titles){
            const module_path = prefix + module_title;
            module_paths.push(module_path);
        }
        return module_paths;
    };
    
    getModuleDirs(module_paths){
        const trees = [];
        for (const module_path of module_paths){
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
    getBotFiles(){
        const bot_files = [];
    
    };
    getDefaultWorkspaceDir(module_dirs){
    
        const tree_data = {
            "/root": {
                path: "/root",
                type: "folder",
                isRoot: true,
                children: this.getModulePaths()
            }
        };
        
        for (const module_dir of module_dirs){
            tree_data.push(module_dir)
        }
        return tree_data
        
    };
    addToState(){
        const module_paths = this.getModulePaths(this.state.modules);
        const module_dirs = this.getModuleDirs(module_paths);
        const def_workspace_dir = this.getDefaultWorkspaceDir(module_dirs);

    };
    

    render(){
        const modules = this.state.modules;
        
        return(
            
            
            <div className = "mainTreeWrapper">
                <h1>
                    This is treeeeee
                </h1>
                {
                    modules.map(
                        module_path => (
                            <div>
                                <h2>
                                    {
                                        module_path
                                    }
                                </h2>
                                <h2>
                                    howdy boyhs
                                </h2>
                            </div>
                        )
                    )
                }

            </div>
        )
    }
    
    
    
}



