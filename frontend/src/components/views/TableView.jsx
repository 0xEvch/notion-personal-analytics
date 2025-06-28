import React from 'react';
import { parseData, extractActivitiesAndMonths } from '../ParseData';

const Table = ({ data }) => {
  // Обрабатываем входные данные
  const parsedData = parseData(data);
  if (!parsedData) {
    return <div>Нет данных для отображения</div>;
  }

  const activities = extractActivitiesAndMonths(parsedData);
//   if (!activities.length || !months.length) {
//     return <div>Недостаточно данных для таблицы</div>;
//   }

//   return (
//     <div style={{ overflowX: 'auto' }}>
//       <table border="1" cellPadding={5} style={{ borderCollapse: 'collapse', minWidth: '600px' }}>
//         <thead>
//           <tr>
//             <th>Активность / Месяц</th>
//             {months.map((month) => (
//               <th key={month}>{month}</th>
//             ))}
//           </tr>
//         </thead>
//         <tbody>
//           {activities.map((activity) => (
//             <tr key={activity}>
//               <td>{activity}</td>
//               {months.map((month) => (
//                 <td key={month}>
//                   {isTotal ? parsedData[month] || 0 : parsedData[activity][month] || 0}
//                 </td>
//               ))}
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
};

export default Table;
