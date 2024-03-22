# File script to close process killmenow

exec { 'kill_killmenow_process':
    path        => '/usr/bin',
    command     => 'pkill -f killmenow',
    refreshonly => true,
    subscribe   => Exec['start_killmenow_process'],
}
