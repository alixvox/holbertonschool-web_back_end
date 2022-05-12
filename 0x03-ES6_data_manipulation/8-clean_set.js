export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || !startString) {
    return '';
  }
  return Array.from(set)
    .map((item) => {
      if (typeof item === 'string' && item.startsWith(startString)) {
        return item.replace(startString, '');
      }
      return undefined;
    })
    .filter((item) => item)
    .join('-');
}
