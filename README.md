# Todo

1. Add a --record-session flag to enable recording without polluting the main code:

# In server.py

parser.add_argument("--record-session", type=str, help="Record LSP session to file")

2. Create a wrapper/middleware pattern for recording:

# New file: src/testing/recorder.py

class LSPRecorder: def **init**(self, server, output_path): self.server = server self.output_path = output_path
self.\_wrap_server_methods()

      def _wrap_server_methods(self):
          # Wrap send/receive methods to record communications
          pass

3. Use recorded sessions for both test types:

   - test_server.py: Use recorded sessions for integration tests
   - test_pipeline.py: Parse recorded sessions to extract scenarios

This gives you:

- Clean production code (recording only activates with flag)
- Real scenario capture from VS Code extension
- Reusable test data across different test types
- Consistent approach for all testing
