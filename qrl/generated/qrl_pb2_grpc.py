# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import qrl.generated.qrl_pb2 as qrl__pb2


class PublicAPIStub(object):
  """//////////////////////////
  //////////////////////////
  //////////////////////////
  ////     API       ///////
  //////////////////////////
  //////////////////////////
  //////////////////////////

  This service describes the Public API used by clients (wallet/cli/etc)
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetNodeState = channel.unary_unary(
        '/qrl.PublicAPI/GetNodeState',
        request_serializer=qrl__pb2.GetNodeStateReq.SerializeToString,
        response_deserializer=qrl__pb2.GetNodeStateResp.FromString,
        )
    self.GetKnownPeers = channel.unary_unary(
        '/qrl.PublicAPI/GetKnownPeers',
        request_serializer=qrl__pb2.GetKnownPeersReq.SerializeToString,
        response_deserializer=qrl__pb2.GetKnownPeersResp.FromString,
        )
    self.GetStats = channel.unary_unary(
        '/qrl.PublicAPI/GetStats',
        request_serializer=qrl__pb2.GetStatsReq.SerializeToString,
        response_deserializer=qrl__pb2.GetStatsResp.FromString,
        )
    self.GetAddressState = channel.unary_unary(
        '/qrl.PublicAPI/GetAddressState',
        request_serializer=qrl__pb2.GetAddressStateReq.SerializeToString,
        response_deserializer=qrl__pb2.GetAddressStateResp.FromString,
        )
    self.GetObject = channel.unary_unary(
        '/qrl.PublicAPI/GetObject',
        request_serializer=qrl__pb2.GetObjectReq.SerializeToString,
        response_deserializer=qrl__pb2.GetObjectResp.FromString,
        )
    self.GetLatestData = channel.unary_unary(
        '/qrl.PublicAPI/GetLatestData',
        request_serializer=qrl__pb2.GetLatestDataReq.SerializeToString,
        response_deserializer=qrl__pb2.GetLatestDataResp.FromString,
        )
    self.GetStakers = channel.unary_unary(
        '/qrl.PublicAPI/GetStakers',
        request_serializer=qrl__pb2.GetStakersReq.SerializeToString,
        response_deserializer=qrl__pb2.GetStakersResp.FromString,
        )
    self.TransferCoins = channel.unary_unary(
        '/qrl.PublicAPI/TransferCoins',
        request_serializer=qrl__pb2.TransferCoinsReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.PushTransaction = channel.unary_unary(
        '/qrl.PublicAPI/PushTransaction',
        request_serializer=qrl__pb2.PushTransactionReq.SerializeToString,
        response_deserializer=qrl__pb2.PushTransactionResp.FromString,
        )
    self.PushEphemeralMessage = channel.unary_unary(
        '/qrl.PublicAPI/PushEphemeralMessage',
        request_serializer=qrl__pb2.PushEphemeralMessageReq.SerializeToString,
        response_deserializer=qrl__pb2.PushTransactionResp.FromString,
        )
    self.CollectEphemeralMessage = channel.unary_unary(
        '/qrl.PublicAPI/CollectEphemeralMessage',
        request_serializer=qrl__pb2.CollectEphemeralMessageReq.SerializeToString,
        response_deserializer=qrl__pb2.CollectEphemeralMessageResp.FromString,
        )
    self.GetTokenDetailedList = channel.unary_unary(
        '/qrl.PublicAPI/GetTokenDetailedList',
        request_serializer=qrl__pb2.Empty.SerializeToString,
        response_deserializer=qrl__pb2.TokenDetailedList.FromString,
        )


class PublicAPIServicer(object):
  """//////////////////////////
  //////////////////////////
  //////////////////////////
  ////     API       ///////
  //////////////////////////
  //////////////////////////
  //////////////////////////

  This service describes the Public API used by clients (wallet/cli/etc)
  """

  def GetNodeState(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetKnownPeers(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStats(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddressState(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetObject(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatestData(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStakers(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TransferCoins(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushEphemeralMessage(self, request, context):
    """------- Ephemeral API -------
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CollectEphemeralMessage(self, request, context):
    """------------------------------
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTokenDetailedList(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PublicAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetNodeState': grpc.unary_unary_rpc_method_handler(
          servicer.GetNodeState,
          request_deserializer=qrl__pb2.GetNodeStateReq.FromString,
          response_serializer=qrl__pb2.GetNodeStateResp.SerializeToString,
      ),
      'GetKnownPeers': grpc.unary_unary_rpc_method_handler(
          servicer.GetKnownPeers,
          request_deserializer=qrl__pb2.GetKnownPeersReq.FromString,
          response_serializer=qrl__pb2.GetKnownPeersResp.SerializeToString,
      ),
      'GetStats': grpc.unary_unary_rpc_method_handler(
          servicer.GetStats,
          request_deserializer=qrl__pb2.GetStatsReq.FromString,
          response_serializer=qrl__pb2.GetStatsResp.SerializeToString,
      ),
      'GetAddressState': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddressState,
          request_deserializer=qrl__pb2.GetAddressStateReq.FromString,
          response_serializer=qrl__pb2.GetAddressStateResp.SerializeToString,
      ),
      'GetObject': grpc.unary_unary_rpc_method_handler(
          servicer.GetObject,
          request_deserializer=qrl__pb2.GetObjectReq.FromString,
          response_serializer=qrl__pb2.GetObjectResp.SerializeToString,
      ),
      'GetLatestData': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatestData,
          request_deserializer=qrl__pb2.GetLatestDataReq.FromString,
          response_serializer=qrl__pb2.GetLatestDataResp.SerializeToString,
      ),
      'GetStakers': grpc.unary_unary_rpc_method_handler(
          servicer.GetStakers,
          request_deserializer=qrl__pb2.GetStakersReq.FromString,
          response_serializer=qrl__pb2.GetStakersResp.SerializeToString,
      ),
      'TransferCoins': grpc.unary_unary_rpc_method_handler(
          servicer.TransferCoins,
          request_deserializer=qrl__pb2.TransferCoinsReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'PushTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.PushTransaction,
          request_deserializer=qrl__pb2.PushTransactionReq.FromString,
          response_serializer=qrl__pb2.PushTransactionResp.SerializeToString,
      ),
      'PushEphemeralMessage': grpc.unary_unary_rpc_method_handler(
          servicer.PushEphemeralMessage,
          request_deserializer=qrl__pb2.PushEphemeralMessageReq.FromString,
          response_serializer=qrl__pb2.PushTransactionResp.SerializeToString,
      ),
      'CollectEphemeralMessage': grpc.unary_unary_rpc_method_handler(
          servicer.CollectEphemeralMessage,
          request_deserializer=qrl__pb2.CollectEphemeralMessageReq.FromString,
          response_serializer=qrl__pb2.CollectEphemeralMessageResp.SerializeToString,
      ),
      'GetTokenDetailedList': grpc.unary_unary_rpc_method_handler(
          servicer.GetTokenDetailedList,
          request_deserializer=qrl__pb2.Empty.FromString,
          response_serializer=qrl__pb2.TokenDetailedList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'qrl.PublicAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AdminAPIStub(object):
  """This is a place holder for testing/instrumentation APIs
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLocalAddresses = channel.unary_unary(
        '/qrl.AdminAPI/GetLocalAddresses',
        request_serializer=qrl__pb2.GetLocalAddressesReq.SerializeToString,
        response_deserializer=qrl__pb2.GetLocalAddressesResp.FromString,
        )


class AdminAPIServicer(object):
  """This is a place holder for testing/instrumentation APIs
  """

  def GetLocalAddresses(self, request, context):
    """FIXME: Use TLS and some signature scheme to validate the cli?
    At the moment, it will run locally
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdminAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLocalAddresses': grpc.unary_unary_rpc_method_handler(
          servicer.GetLocalAddresses,
          request_deserializer=qrl__pb2.GetLocalAddressesReq.FromString,
          response_serializer=qrl__pb2.GetLocalAddressesResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'qrl.AdminAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
