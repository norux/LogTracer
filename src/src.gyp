# Generated by Andrew Heebum Kwak (kh-1143@hanmail.net)

{
    'includes':
    [
        '../LogTracer.gypi',
    ],

    'targets':
    [
        {
            'target_name': 'test',
            'type': 'static_library',
            
            'dependencies':
            [

            ],

            'defines':
            [

            ],

            'include_dirs':
            [
                '../include',
            ],

            'sources':
            [
            ],

            'conditions':
            [
                [
                    'OS=="linux"',
                    {
                        'library_dirs':
                        [

                        ],
                    },
                ],
            ],
        },
    ],
}
