import React, { Component } from "react";

class Counter extends Component {
    // Properties for class contained in state
    state = {
        count: 0
    };

    // Called when compiled into JS
    render() {
        return (
            <div>
                {/* Call method and render it */}
                <p>{this.formatCount()}</p>
                <button>Test</button>
            </div>
        );
    }

    formatCount() {
        // Pull count prop from state object
        const {count} = this.state;

        // You can return JSX to be rendered
        return count === 0 ? <p>Zero</p> : count;
    }
}

export default Counter;
