import React from "react";
import axios from "axios";

export default class ProductList extends React.Component{
    state = {
        products: [],
        error: null,
        isLoading: true
    }
    constructor(props){
        super(props);
    }
    fetchProducts() {
        fetch("http://192.168.1.149:8000/api/products/")
        .then(
            response => response.json()
        )    
        .then(
            data => this.setState(
                {
                    products: data,
                    isLoading: false
                }
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
        this.fetchProducts();
    }
    render(){
        return(
            <div>
            
            {
            !this.state.isLoading, this.state.products.map(
                product =>{
                    return(
                        <h1>
                            {
                                product.title
                            }
                        </h1>
                    )
                }
            )
            }
            </div>
        )
    }
}