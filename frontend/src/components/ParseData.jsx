export function parseData(data) {
    if (!data) return;

    try {
      // Если data.data — строка, парсим её
      const dataToParse = data.data || data;
      let parsedData = typeof dataToParse === 'string' ? JSON.parse(dataToParse) : dataToParse;

      // Если data.data уже объект
      if (parsedData.data) {
        parsedData = typeof parsedData.data === 'string' ? JSON.parse(parsedData.data) : parsedData.data;
      }

      return parsedData;
    } catch (err) {
      console.error('Error parsing data:', err);
      return;
    }
}

export function extractActivitiesAndMonths(parsedData) {
    if (!parsedData) return { activities: [], months: [], isTotal: false };
    
    const keys = Object.keys(parsedData);
    // Извлекаем активности и месяцы
    if (keys.length > 0 && typeof parsedData[keys[0]] === 'object' && !Array.isArray(parsedData[keys[0]])) {
      const activities = keys;
      const months = Object.keys(parsedData[activities[0]] || {});
      return { activities, months, isTotal: false };
    } else {
      // Второй JSON: месяцы как ключи, значения — числа
      const months = keys;
      const activities = ['Total']; // Одна "активность" для отображения
      return { activities, months, isTotal: true };
    }
}