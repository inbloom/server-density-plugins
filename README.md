Summary
=======
A collection of various ServerDensity plugins that we have developed for use. These plugins can also be found in the ServerDensity Plugin store. http://plugins.serverdensity.com/list/

Plugins
=======
Below is a list of plugins within this repo and a brief description of its use.
FreeMemory
----------
This plugin expands on the built in Server Density available memory metric to take into account caching/buffers.
LastChefRun
-----------
This plugin reports the time in seconds since the last succesful chef-client run.
This plugin requires the following report handler to be configured. https://github.com/omniti-labs/chef-tools/blob/master/handlers/last_good_run.rb
More information about chef handlers: http://docs.opscode.com/handlers.html
