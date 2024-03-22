exec { 'kill_killmenow_process':
    command     => 'pkill -f killmenow',
    refreshonly => true,
    # Subscribe to a command that starts the process
    subscribe   => Exec['start_killmenow_process'],
}
