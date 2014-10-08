class PhoneDirectoryActions(object):
    '''
    Defines an interface for actions the frontend can perform on the database. Children of this class
    will be database-specific implementations.
    '''
    def user_exists(userid):
        '''
        Return true if userid exists, false if not
        '''
        raise NotImplementedError('user_exists')

    def get_phone_number(userid):
        '''
        Return phone number for given userid. Fail if user doesn't exist
        '''
        raise NotImplementedError('get_phone_number')

    def update_phone_number(userid, new_number):
        '''
        If userid exists, update its phone number and archive the old number.
        If userid does not exist, fail.
        '''
        raise NotImplementedError('update_phone_number')
