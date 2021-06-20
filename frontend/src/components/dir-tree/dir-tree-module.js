import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

export default class DirTreeModule extends React.Component{
    render(){
        const{
            title,
            icon_cdn_class
        } = this.props;
        return(
            <div>
                <FontAwesomeIcon
                    icon = {icon_cdn_class}
                >
                <h1>{title}</h1>

                </FontAwesomeIcon>
            </div>
        )
    }
    
}