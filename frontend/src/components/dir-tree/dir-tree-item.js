import React from "react";

export default class DirTreeItem extends React.Component{
    render(){
        const{
            title,
            icon_cdn_class
        } = this.props;

        return(
            <div>
                <i class = {icon_cdn_class}></i>
                <h2>{title}</h2>
            </div>
        )
    }
}