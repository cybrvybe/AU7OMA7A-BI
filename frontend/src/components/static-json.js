import {faCogs, faDatabase, faHome, faPlusSquare, faSignOutAlt} from '@fortawesome/free-solid-svg-icons';
const main_nav_items = [
    {
        "title": "Home",
        "icon_cdn_class": faHome,
        "tooltip": "Takes you to AU7OMA7A's homepage."
        
        
    },
    {
        "title": "Data Directory",
        "icon_cdn_class": faDatabase,
        "tooltip": "Go to data directory to explore your data."
    },
    {
        "title": "Integrations",
        "icon_cdn_class": faPlusSquare,
        "tooltip": "Use 'Integrations' navigation button to manage data integrations and extensions."
    }
];


const secondary_nav_items = [
    {
        "title": "Settings",
        "icon_cdn_class": faCogs,
        "tooltip": "Change Settings"
    },
    {
        "title": "Log Out",
        "icon_cdn_class": faSignOutAlt,
        "tooltip": "Log out"
    }
];
const native_dir_tree_folders = [
    {
        "title": "Automaton",
        "icon_cdn_class":""
    },
    {
        "title": "Data Objects",
        "icon_cdn_class": ""
    },
    {
        "title": "Reports",
        "icon_cdn_class":""
    }
];
const native_dir_tree_subfolders = [
    {
        "title": "Templates",
        "icon_cdn_class": "fas fa-robot"
    }
];



const dict = {
    "main_nav_items": main_nav_items,
    "secondary_nav_items": secondary_nav_items,
    "native_dir_tree_folders": native_dir_tree_folders,
    "native_dir_tree_subfolders": native_dir_tree_subfolders
}
export default dict
