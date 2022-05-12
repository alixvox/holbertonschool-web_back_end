export default function createInt8TypedArray(length, position, value) {
  if (position > length || position < 0) throw Error('Position outside range');
  const i8Array = new ArrayBuffer(length);
  new Int8Array(i8Array)[position] = value;
  return new DataView(i8Array, 0);
}
