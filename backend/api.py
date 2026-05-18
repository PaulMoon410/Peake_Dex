import sys
try:
    from app import app
except Exception as e:
    print("[IMPORT ERROR] Failed to import app:", e, file=sys.stderr)
    import traceback; traceback.print_exc()
    raise

if __name__ == "__main__":
    import os
    try:
        port = int(os.environ.get("PORT", 8080))
        app.run(host="0.0.0.0", port=port)
    except Exception as e:
        print("[STARTUP ERROR] Failed to start Flask app:", e, file=sys.stderr)
        import traceback; traceback.print_exc()
        raise
