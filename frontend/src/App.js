
import './App.scss';

import dict from './components/static-json';
import SidebarNav from './components/nav/nav-list';
function App() {
  return (
    <div className="App">
      <script src="js/reactjs/main.js" type = "text/babel"></script>
      <div className="App-header">
        
        
        
        <SidebarNav
          
          main_nav_items = {dict["main_nav_items"]}
          secondary_nav_items = {dict["secondary_nav_items"]}>
            <h1>Sidebar Nav</h1>
        </SidebarNav>
        
        
      </div>
    </div>
  );
}

export default App;
