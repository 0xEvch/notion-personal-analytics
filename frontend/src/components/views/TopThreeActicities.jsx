import React from 'react';
import { parseData } from '../ParseData';
import './TopThreeActicities.css'

const TopThreeActicities = ({ data })  => {
    const parsedData = parseData(data);
    if (!parsedData) {
      return;
    }

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
    console.log(grouped)

    return (
        <div>
          {Object.entries(grouped).map(([month, projects]) => (
            <div key={month}>
              <h1>{month}</h1>
              {/* Сортируем проекты по времени, чтобы вывести топ 3 */}
              {projects
                .sort((a, b) => b.time - a.time)
                .slice(0, 3)
                .map(({ project, time }) => (
                  <h2 key={project}>
                    {project} - {time} hours
                  </h2>
                ))}
            </div>
          ))}
        </div>
    );
};
  
  export default TopThreeActicities