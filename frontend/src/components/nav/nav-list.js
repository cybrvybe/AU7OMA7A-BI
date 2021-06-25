import React from "react";
import "../nav/sidebar-nav.scss";
import {
    Tab, 
    Tabs, 
    TabList,
    TabPanel
} from "react-tabs";
import dict from "../static-json";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import Tree from "../dir-tree/tree.js";
export default class SidebarNav extends React.Component{
    render(){
        const{
            main_nav_items = [],
            secondary_nav_items = []
        } = this.props;
       

        return(
            <div className = "sidebar">
                <Tabs className = "sidebarWrapper">

                    
                    <TabList className = "tabList">
                        <div className = "sidebarNav">
                            <div>
                                {
                                    main_nav_items.map(
                                        item =>(
                                            <Tab>
                                                <FontAwesomeIcon 
                                                    icon = {item.icon_cdn_class}
                                                    className = "navIcon"
                                                >
                                                    
                                                </FontAwesomeIcon>
                                            </Tab>
                                        )
                                    )
                                    
                                }
                            </div>
                            <div>
                                {
                                    secondary_nav_items.map(
                                        item =>(
                                            <div>
                                                <FontAwesomeIcon 
                                                    icon = {item.icon_cdn_class}
                                                    className = "navIcon"   
                                                >
            
                                                </FontAwesomeIcon>
                                            </div>
                                    )
                                    )
                                }
                            </div>
                            
                        </div>

                    </TabList>
                    <TabPanel className = "tabPanel">
                        <div className = "innerTabPanelWrapper">
                            <h1>Homepage</h1>
                        </div>
                    </TabPanel>
                    <TabPanel className = "tabPanel">
                        <Tree
                            native_folders = {dict["native_dir_tree_folders"]}
                            native_subfolders = {dict["native_dir_tree_subfolders"]}
                        
                        >

                        </Tree>
                    </TabPanel>
                </Tabs>
               
            </div>
        )
    }
}

