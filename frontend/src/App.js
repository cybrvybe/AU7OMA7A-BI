import logo from './logo.svg';
import './App.css';
import ModelDashboard from './components/dashboard/dashboard';
import ProductList from './components/list-view';
import dict from './components/static-json';
import SidebarNav from './components/nav-list';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1> yo this is me</h1>
        <ModelDashboard>
          
        </ModelDashboard>
        <ProductList>
          This is the product list component
        </ProductList>
        <SidebarNav
          
          main_nav_items = {dict["main_nav_items"]}
          secondary_nav_items = {dict["secondary_nav_items"]}>
            <h1>SidebarNav</h1>
        </SidebarNav>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
