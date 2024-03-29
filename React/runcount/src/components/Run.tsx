import React from "react";

interface Props {
    count: number
}

const Run: React.FC<Props> = (count: Props) => {
    const runs: string[] = ["test1", "test2"];

    const test = (): JSX.Element[] => {
        return runs.map((person) => {
            return (
                <p>{person}</p>
            );
        });
    };

    return (
        <div>
            <h1>List of {count.count} runs</h1>
            <ul>
                <li>{test()}</li>
            </ul>
        </div>
    )
}

export default Run;
