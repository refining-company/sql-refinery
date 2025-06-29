import * as vscode from 'vscode';
import { initDiagnostics } from './variations';
import { initShowJourney, showVariationsCommand } from './variationsShow';
import { initExploreJourney } from './variationsExplore';

// ========================================
// VARIATIONS FEATURE INTEGRATION
// ========================================

// Main entry point for variations feature
export function initVariations(context: vscode.ExtensionContext): void {
  // Initialize core setup and detection (Journey: Setup)
  const diagnosticCollection = initDiagnostics(context);
  
  // Initialize discovery journey (Journey: Show)
  const inlineProvider = initShowJourney(context, diagnosticCollection);
  
  // Initialize exploration journey (Journey: Explore)
  const variationsProvider = initExploreJourney(context);
  
  // Register the show variations command (bridges Show -> Explore)
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.showVariations', (args) => 
      showVariationsCommand(args, context, variationsProvider)
    )
  );
  
  // TODO: Register ignore command for completeness
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.ignoreVariation', (args) => {
      // Placeholder for ignore functionality
      vscode.window.showInformationMessage(`Ignored variation group ${args.groupId}`);
    })
  );
}