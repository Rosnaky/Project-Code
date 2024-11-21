"""Generated client library for messagestreams version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.messagestreams.v1alpha import messagestreams_v1alpha_messages as messages


class MessagestreamsV1alpha(base_api.BaseApiClient):
  """Generated client library for service messagestreams version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://messagestreams.googleapis.com/'
  MTLS_BASE_URL = 'https://messagestreams.mtls.googleapis.com/'

  _PACKAGE = 'messagestreams'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'MessagestreamsV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new messagestreams handle."""
    url = url or self.BASE_URL
    super(MessagestreamsV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_streams_retryPolicies = self.ProjectsLocationsStreamsRetryPoliciesService(self)
    self.projects_locations_streams = self.ProjectsLocationsStreamsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(MessagestreamsV1alpha.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (MessagestreamsProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='messagestreams.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='MessagestreamsProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (MessagestreamsProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='messagestreams.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (MessagestreamsProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='messagestreams.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (MessagestreamsProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='messagestreams.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/operations',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsStreamsRetryPoliciesService(base_api.BaseApiService):
    """Service class for the projects_locations_streams_retryPolicies resource."""

    _NAME = 'projects_locations_streams_retryPolicies'

    def __init__(self, client):
      super(MessagestreamsV1alpha.ProjectsLocationsStreamsRetryPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new retry policy.

      Args:
        request: (MessagestreamsProjectsLocationsStreamsRetryPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}/retryPolicies',
        http_method='POST',
        method_id='messagestreams.projects.locations.streams.retryPolicies.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['retryPolicyId'],
        relative_path='v1alpha/{+parent}/retryPolicies',
        request_field='retryPolicy',
        request_type_name='MessagestreamsProjectsLocationsStreamsRetryPoliciesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a retry policy.

      Args:
        request: (MessagestreamsProjectsLocationsStreamsRetryPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}/retryPolicies/{retryPoliciesId}',
        http_method='DELETE',
        method_id='messagestreams.projects.locations.streams.retryPolicies.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsStreamsRetryPoliciesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get a retry policy.

      Args:
        request: (MessagestreamsProjectsLocationsStreamsRetryPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RetryPolicy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}/retryPolicies/{retryPoliciesId}',
        http_method='GET',
        method_id='messagestreams.projects.locations.streams.retryPolicies.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsStreamsRetryPoliciesGetRequest',
        response_type_name='RetryPolicy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List retry policies.

      Args:
        request: (MessagestreamsProjectsLocationsStreamsRetryPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListRetryPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}/retryPolicies',
        http_method='GET',
        method_id='messagestreams.projects.locations.streams.retryPolicies.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/retryPolicies',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsStreamsRetryPoliciesListRequest',
        response_type_name='ListRetryPoliciesResponse',
        supports_download=False,
    )

  class ProjectsLocationsStreamsService(base_api.BaseApiService):
    """Service class for the projects_locations_streams resource."""

    _NAME = 'projects_locations_streams'

    def __init__(self, client):
      super(MessagestreamsV1alpha.ProjectsLocationsStreamsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new stream in a given project and location.

      Args:
        request: (MessagestreamsProjectsLocationsStreamsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/streams',
        http_method='POST',
        method_id='messagestreams.projects.locations.streams.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['requestId', 'streamId'],
        relative_path='v1alpha/{+parent}/streams',
        request_field='stream',
        request_type_name='MessagestreamsProjectsLocationsStreamsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single stream.

      Args:
        request: (MessagestreamsProjectsLocationsStreamsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}',
        http_method='DELETE',
        method_id='messagestreams.projects.locations.streams.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['etag', 'requestId'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsStreamsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single stream.

      Args:
        request: (MessagestreamsProjectsLocationsStreamsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Stream) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}',
        http_method='GET',
        method_id='messagestreams.projects.locations.streams.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsStreamsGetRequest',
        response_type_name='Stream',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists streams in a given project and location.

      Args:
        request: (MessagestreamsProjectsLocationsStreamsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListStreamsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/streams',
        http_method='GET',
        method_id='messagestreams.projects.locations.streams.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/streams',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsStreamsListRequest',
        response_type_name='ListStreamsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single stream.

      Args:
        request: (MessagestreamsProjectsLocationsStreamsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}',
        http_method='PATCH',
        method_id='messagestreams.projects.locations.streams.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='stream',
        request_type_name='MessagestreamsProjectsLocationsStreamsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(MessagestreamsV1alpha.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (MessagestreamsProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='messagestreams.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (MessagestreamsProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations',
        http_method='GET',
        method_id='messagestreams.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'includeUnrevealedLocations', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/locations',
        request_field='',
        request_type_name='MessagestreamsProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(MessagestreamsV1alpha.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
