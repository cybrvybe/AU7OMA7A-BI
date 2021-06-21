
import React from "react";
import DirTreeItem from "./dir-tree-item";
import DirTreeModule from "./dir-tree-module";
import "./dir-tree.scss";

export default class MainDirTree extends React.Component{
    state = {
        modules: [],
        dirTreeFolders: [],
        error: null,
        isLoading: true
    }
    
    fetchModules(){
        fetch("http://192.168.1.149:8000/api/modules/")
        .then(
            response => response.json()
        )
        .then(
            data => this.setState(
                {
                    modules: data,
                    isLoading: false
                }
            )
        )
        .then(
            fetch(
                "http://192.168.1.149:8000/api/dir_tree_folders/"
            )
            .then(
                response => response.json()
            )
            .then(
                data => this.setState(
                    {
                        dirTreeFolders: data,
                        isLoading: false
                    }
                )
            )
        )
        .catch(
            error => this.setState(
                {
                    error,
                    isLoading: false
                }
            )
        );
    }
    componentDidMount(){
        this.fetchModules();
    }
    render(){
        const{
            native_folders = [],
            native_subfolders = []

        } = this.props;

        return(
            <div className = "dirTree">
                {
                    !this.state.isLoading,this.state.modules.map(
                        module => (
                            <div>
                                <div>
                                    <DirTreeModule
                                        icon_cdn_class = {module.icon_cdn_class}    
                                    >

                                    </DirTreeModule>
                                    <h1>{module.title}</h1>
                                </div>
                                <div>
                                {
                                native_folders.map(
                                    folder => (
                                        <div>
                                            <DirTreeItem
                                                title = {folder.title}
                                                icon_cdn_class = {folder.icon_cdn_class}
                                            >
                                            </DirTreeItem>
                                            <div>
                                                {native_subfolders.map(
                                                    subfolder => (
                                                        <DirTreeItem
                                                            title = {subfolder.title}
                                                            icon_cdn_class = {subfolder.icon_cdn_class}
                                                        >
                                                        </DirTreeItem>
                                                    )
                                                )}
                                            </div>
                                            
                                        </div>
                                    )
                                )
                            }
                                </div>
                            </div>
                        )
                    )
                }
                
            </div>
        )
    }
}