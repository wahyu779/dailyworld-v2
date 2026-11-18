// dailyworld-v2 entrypoint: copy the pre-rendered newspaper page to the output.
// The program runs with no network; the image is built from local assets only.
// Uses only Deno built-ins, so it runs identically on every run.
const outDir = Deno.env.get("OUTPUT_DIR") ?? "/output";
await Deno.mkdir(outDir, { recursive: true });
await Deno.copyFile("entry.png", `${outDir}/entry.png`);
console.log(`wrote ${outDir}/entry.png`);
