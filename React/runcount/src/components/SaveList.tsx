import React, { useState } from "react";
import { setTokenSourceMapRange } from "typescript";

interface Run {
    name: string,
    distance: number,
    // Passed in function from parent App component
    handleAdd: (e: React.FormEvent) => void;
}

const SaveList: React.FC<Run> = ({name, distance, handleAdd}) => {
    const [post, setPost] = useState(
        {
            name: "",
            distance: 0,
        }
    );

    const POST = (event: React.ChangeEvent<
        HTMLInputElement |
        HTMLTextAreaElement
        >): void => {
        setPost(
            {
                ...post,
                [event.target.name]: event.target.value
            }
        )
    };

    const setName = (newName: string): void => {
        name = newName;
    }

    return (
        <form onSubmit={(e) => handleAdd(e)}>
            <label htmlFor="name">Name: </label>
            <input
                type="text"
                name="name"
            /><br></br>
            <label htmlFor="distance">Distance: </label>
            <input
                type="number"
                name="distance"
                placeholder="Distance"
                step=".01"
            />km<br></br>
            <button type="submit">Add</button>
        </form>
    );
}

export default SaveList;
