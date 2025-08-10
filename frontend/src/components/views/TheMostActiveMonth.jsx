import './TheMostActiveMonth.css'

const TheMostActiveMonth = ({ data }) => {
    const jsonData = JSON.parse(data.data);

    const month = jsonData.Month;
    const totalTimeMin = jsonData["Total Time (min)"];
    const totalTimeHrs = jsonData["Total Time"];
    const uniqueDays = jsonData["Unique Days"];

    return (
        <div className="card">
            <h1>The most active month: {month} </h1>
            <p>{totalTimeHrs} hours and {uniqueDays} unique days</p>
        </div>
    )
}

export default TheMostActiveMonth