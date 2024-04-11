import decorator
import deprecated
try:
    deprecated.classic(decorator.fix)
except:
    decorator.ContextManager.__call__.__builtins__.fromkeys