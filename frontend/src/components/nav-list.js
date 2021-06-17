import React from "react";


export default class SidebarNav extends React.Component{
    render(){
        const{
            main_nav_items,
            secondary_nav_items
        } = this.props;

        return(
            <div>
                <div>
                    {
                        main_nav_items.map(
                            item =>{
                                <div>
                                    <a>
                                        {main_nav_items.title}
                                    </a>
                                </div>
                            }
                        )
                    }

                </div>
                <div>
                    {
                        secondary_nav_items.map(
                            item =>{
                                <div>
                                    <a>
                                        {secondary_nav_items.title}
                                    </a>
                                </div>
                            }
                        )
                    }

                </div>
            </div>
        )
    }
}

