import React from 'react';
import { parseData } from '../ParseData';
import './TopThreeActicities.css'

const TopThreeActicities = ({ activities, category })  => {
  const parsedActivities = parseData(activities);
  const parsedCategories = parseData(category);
  if (!parsedActivities && !parsedCategories) {
    return;
  }

  const groupedActivities = parse(parsedActivities);
  const groupedCategories = parse(parsedCategories);
  console.log(activities)

  return (
<div>
    {Object.keys(groupedCategories).map((month) => (
      <div className="month-container" key={month}>
        <h1>{month}</h1>
        <div className="columns-wrapper">
          
          {/* Левая колонка — категории */}
          <div className="column">
            <h3>Categories</h3>
            {groupedCategories[month]
              .sort((a, b) => b.time - a.time)
              .slice(0, 3)
              .map(({ project, time }) => (
                <h2 key={project}>
                  {project} - {time} hours
                </h2>
              ))}
          </div>
          
          {/* Правая колонка — активности */}
          <div className="column">
            <h3>Activities</h3>
            {(groupedActivities[month] ?? [])
              .sort((a, b) => b.time - a.time)
              .slice(0, 3)
              .map(({ project, time }) => (
                <h2 key={project}>
                  {project} - {time} hours
                </h2>
              ))}
          </div>

        </div>
      </div>
    ))}
  </div>
  );
};

const parse = (parsedData) => {
  const grouped = {};
  
  Object.entries(parsedData).forEach(([key, value]) => {
    // Регулярное выражение для извлечения месяца и проекта
    // Предполагаю, что ключи вида: "('April', 'Sims 4 CC')"
    const match = key.match(/^\('([^']+)',\s*'([^']+)'\)$/);
    if (match) {
      const month = match[1];
      const project = match[2];
      if (!grouped[month]) {
        grouped[month] = [];
      }
      const time = value['Total Time']; 
      grouped[month].push({ project, time });
    }
  });

  return grouped;
}
  
export default TopThreeActicities