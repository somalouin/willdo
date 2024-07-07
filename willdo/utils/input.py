def handle_params(params, function):
  if len(params) > 2:
    function(params[2])
  else:
    function()