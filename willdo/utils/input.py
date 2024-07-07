def handle_params(params, function):
  if len(params) > 2 and params[2].endswith('.py'):
    function(params[2])
  else:
    function()