import { defineConfig } from '@vscode/test-cli';

export default defineConfig({
	files: 'out/test/**/*.test.js',
	workspaceFolder: './src/test/inputs',
	launchArgs: [
		'--disable-workspace-trust',
		'--skip-welcome',
		'--skip-release-notes',
		'--window-size=1920,1200'
	]
});
