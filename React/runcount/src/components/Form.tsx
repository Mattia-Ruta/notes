import React, { useState } from "react";

const SaveList = (): JSX.Element => {
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
    }

    return (
        <div>
            <input
                type="test"
                name="name"
                placeholder="Name"
                value={post.name}
                onChange={POST}>
            </input>
            <input
                type="number"
                name="distance"
                placeholder="Distance"
                value={post.distance}
                onChange={POST}>
            </input>
        </div>
    );
}

export default SaveList;
