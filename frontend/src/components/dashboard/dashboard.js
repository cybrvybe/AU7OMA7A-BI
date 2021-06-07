import React from "react";
import ChildModelListsLayout from "./child_list_layout";
import LiveDashboard from "./live_dashboard";
import ModelSynopsis from "./model_synopsis";

class ModelDashboard extends React.Component{
    state = {
        models: []
    };

    async componentDidMount(){
        try{
            const res = await fetch("http://127.0.0.1:8000/api/");
            const models = await res.json();
            this.setState(
                {
                    models
                }
            );
        } catch (e) {
            console.log(e);
        }
    }
    render(){
        return(
            <div>
                {
                    this.state.models.map(
                        model => (
                            <div>
                                <h1>{model.title}</h1>
                                <h1>This is a model</h1>
                            </div>
                        )
                    )
                }
                <h1>This is the dashboard.</h1>
                <LiveDashboard>

                </LiveDashboard>
                <ModelSynopsis>

                </ModelSynopsis>
                <ChildModelListsLayout>
                    
                </ChildModelListsLayout>
            </div>
        )
    }

}
export default ModelDashboard;