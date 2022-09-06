import React, { Component } from "react";

class Counter extends Component {
    // Properties for class contained in state
    state = {
        title: "Counter Page",
        count: 0,
        templates: ["Income", "Budgets"]
    };

    constructor() {
        // Always initiate parent class first
        super();

        // Binding method to object passes "this" reference along into method
        this.handleAdd = this.handleAdd.bind(this);
    }

    // Called when compiled into JS
    render() {
    
        return (
            // Wrap in <React.Fragment> for multiple HTML elements
            // Or use <div> to contain in template
            <React.Fragment>
                {/* Call method and render it */}
                <h1>{this.state.title}</h1>
                <span 
                    style={this.checkColour()}
                    className={this.getBadgeClasses()}>
                    {this.state.count}
                </span>
                {/* Use reference to method, don't call for adding event handling */}
                <button 
                    onClick={this.handleAdd}
                >
                    Add
                </button>
                <button>Subtract</button>
                <div>
                    {this.getList()}
                </div>
            </React.Fragment>
        );
    }

    handleAdd() {
        this.setState({count: this.state.count + 1})
    }

    newMethod = () => {
        // Create new arrow-function to automatically have reference to "this"
        console.log(this);
    }
    getBadgeClasses() {
        let classes = "badge m-2";
        classes += (this.state.count === 0) ? "badge-warning" : "badge-primary";
        return classes;
    }

    checkColour() {
        const { count } = this.state;   // Use curly braces to pull from state
        const countCopy = this.state.count; // Don't use to just copy value
        console.log(countCopy);

        const red = { color: "red" };

        return count === 0 ? red : {};
    }

    getList() {
        const templates = this.state.templates;
        if (templates.length === 0) {
            return <p>There are no templates!</p>;
        } else {
            // Map each element in list as its own list item using map()
            // Make sure to use a unique key for React to identify the element
            return (
                <ul>
                    {templates.map(template => <li key={template}>{template}</li>)}
                </ul>
            );
        }
    }
}

export default Counter;
